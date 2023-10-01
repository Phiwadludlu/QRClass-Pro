const app = Vue.createApp({
    data() {
        return {
            moduleItems: [], // Initialize with the expected data structure
            qualificationItems: [],
        };
    },
    methods: {
        async fetchModuleItems() {
            try {
                // Replace with your actual API endpoint for moduleItems
                const response = await fetch('/api/v1/module/all', {
                    mode: 'cors',
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });
                const moduleItems = await response.json();
                this.moduleItems = moduleItems;
            } catch (error) {
                console.error('Error fetching moduleItems:', error);
            }
        },
        async fetchQualificationItems() {
            try {
                // Replace with your actual API endpoint for moduleItems
                const response = await fetch('/api/v1/qualification/all', {
                    mode: 'cors',
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });
                const qualificationItems = await response.json();
                this.qualificationItems = qualificationItems;
            } catch (error) {
                console.error('Error fetching qualificationItems:', error);
            }
        },
    },
    created () {
        this.fetchModuleItems();
        this.fetchQualificationItems();
    }
});

app.component('multiselect', {
    template: '#multiselect-template',
    props: {
        searchFieldId: String,
        dropdownId: String,
        limit: Number,
        action: String,
        returnType: String,
        items: Array,
        checkboxType: String,
    },
    data() {
        return {
            searchText: '',
            currentTags: [],
        };
    },
    computed: {
        filteredItems() {
            return this.items.filter(item => {
                const isMatch = item.name.toLowerCase().includes(this.searchText.toLowerCase()) || item.code.toLowerCase().includes(this.searchText.toLowerCase());
                return isMatch;
            });
        },
        isDropdownDisabled() {
            return this.currentTags.length === this.limit;
        },
    },
    methods: {
        fetchSearch(value) {
            this.searchText = value;
        },
        debounceInput(id) {
            let timeoutId;
            const waitTime = 800;

            const input = document.getElementById(id);
            input.addEventListener('keyup', (e) => {
                const text = e.currentTarget.value;

                clearTimeout(timeoutId);

                timeoutId = setTimeout(() => {
                    this.fetchSearch(text);
                }, waitTime);
            });
        },
        async handleDropdownClick(value) {
            console.log(this.limit, this.returnType, value);
            if (this.currentTags.includes(value)) {
                this.currentTags = this.currentTags.filter(tag => tag !== value);
            } else {
                this.currentTags.push(value);
            }

            if (document.querySelector("div.carousel-indicators>button.active")) {
                const currentStep = document.querySelector("div.carousel-indicators>button.active").ariaLabel;

                if (!document.querySelector("div.row>div.d-flex.justify-content-center>button.btn.btn-secondary.w-75") && (currentStep === "Step 2") && (this.currentTags.length >= 3)) {
                    const gs2 = document.getElementById("getting-started-2");
                    const section = document.createElement('div');
                    section.setAttribute('class', 'row');
                    const center = document.createElement('div');
                    center.setAttribute('class', 'd-flex justify-content-center');
                    const btn = document.createElement('button');
                    btn.setAttribute('class', 'btn btn-secondary w-75');

                    btn.textContent = "Lets go!";

                    center.appendChild(btn);
                    section.appendChild(center);
                    gs2.appendChild(section);
                }
            }

            const limitReached = this.currentTags.length === this.limit;
            console.log(limitReached);

            if (limitReached) {
                const response = await fetch('/api/v1/config/multiselect', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        action: this.action,
                        returnType: this.returnType,
                        value: this.currentTags,
                    })
                });

                console.log(this.action);

                let result;
                if (this.returnType == "module-table") {
                    const renderTo = document.getElementById("table-area");
                    renderTo.innerHTML = '';

                    result = await response.text();
                    renderTo.innerHTML = result;
                } else {
                    const nextCtrl = document.getElementById("next-carousel");
                    const prevCtrl = document.getElementById("prev-carousel");

                    if (this.action === "qualification-selection") {
                        nextCtrl.style.display = "block";
                        prevCtrl.style.display = "none";
                    } else if (this.action === "module-selection") {
                        nextCtrl.style.display = "none";
                        prevCtrl.style.display = "block";
                    }
                }
            }
        },
        handleTagClick(tag) {
            // Remove the clicked tag from currentTags
            console.log("handleTagClick -> [type]",this.returnType);
            if (this.returnType === "module-table") {
                const renderTo = document.getElementById("table-area");
                renderTo.innerHTML = '';
            }
            this.currentTags = this.currentTags.filter(t => t !== tag);

            if (document.querySelector("div.carousel-indicators>button.active")) {
                const currentStep = document.querySelector("div.carousel-indicators>button.active").ariaLabel;
                if ((this.currentTags.length !== this.limit) && (currentStep === "Step 1")) {
                    const nextCtrl = document.getElementById("next-carousel");
                    nextCtrl.style.display = "none";
                } if ((this.currentTags.length < 3) && (currentStep === "Step 2")) {
                    document.querySelector("div.row>div.d-flex.justify-content-center>button.btn.btn-secondary.w-75").remove();
                }
            }
        },
    },
    mounted() {
        this.debounceInput('multiselect-searchfield');
    }
});

app.component('searchfield', {
    template: '#searchfield-template',
    data() {
        return {
            searchText: '',
        };
    },
    methods: {
        async handleEnterKey(event) {
            // Check if the "enter" key (key code 13) is pressed and the input field is focused
            if (event.keyCode === 13 && document.activeElement === event.target) {
                document.activeElement.blur()
                try {
                    const response = await fetch('/api/v1/config/searchfield', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            value: this.searchText,
                        }),
                    });
                    const result = await response.text();

                    // Render the response inside the #table-area element
                    const renderTo = document.getElementById("table-area");
                    renderTo.innerHTML = result;
                } catch (error) {
                    console.error('Error sending POST request:', error);
                }
            }
        },
        handleClick() {
            this.searchText = '';
            const renderTo = document.getElementById("table-area");
            renderTo.innerHTML = '';
        }
    },
});

const vm = app.mount('#app');