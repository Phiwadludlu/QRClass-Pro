const app = Vue.createApp({
    data() {
        return {
            timeslotsData: [],
            moduleItems: [], // Initialize with the expected data structure
            qualificationItems: [],
            selectedModule: '',
        };
    },
    methods: {
        updateSelectedModule(newVal) {
            this.selectedModule = newVal;
        },
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
    created() {
        this.fetchModuleItems();
        this.fetchQualificationItems();
        var queryParams = window.location.search.substring(1).split('&');
        for (var i = 0; i < queryParams.length; i++) {
            var param = queryParams[i].split('=');
            if (param[0] === 'module') {
                // Set "selectedModule" to the value of the "module" query parameter
                this.selectedModule = decodeURIComponent(param[1]);
                break;
            }
        }
    }
});

app.component('multiselect', {
    template: '#multiselect-template',
    setup() {
        const ms = Vue.ref(null);
        return {
            ms
        }
    },
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
            this.$emit('selected-module', this.currentTags[0]);
        },
        handleTagClick(tag) {
            // Remove the clicked tag from currentTags
            console.log("handleTagClick -> [type]", this.returnType);
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
    },
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

app.component('numberpicker', {
    template: '#numberpicker-template',
    setup() {
        const np = Vue.ref(null);
        return {
            np
        }
    },
    props: {
        initialValue: {
            type: Number,
            default: 1,
        },
    },
    data() {
        return {
            value: this.initialValue,
            selectedDuration: 'min', // Default selected duration
        };
    },
    computed: {
        maxValue() {
            // Set the max value based on the selected duration
            switch (this.selectedDuration) {
                case 'hr':
                    return 24;
                case 'day':
                    return 14;
                case 'min':
                default:
                    return 60;
            }
        },
    },
    watch: {
        value(newVal, oldVal) {
            // When the value changes, validate it against the max value
            if (newVal > this.maxValue) {
                this.value = oldVal; // Revert to the old value if it exceeds the max
            }
        },
    },
    methods: {
        decrement() {
            if (this.value > 1) {
                this.value--;
            }
        },
        increment() {
            if (this.value < this.maxValue) {
                this.value++;
            }
        },
        updateValue(event) {
            const newValue = parseInt(event.target.value, 10);
            if (!isNaN(newValue) && newValue >= 1) {
                this.value = newValue;
            }
        },
        resetValue() {
            // Reset the value to 1 if it's above the max value for the selected duration
            if (this.value > this.maxValue) {
                this.value = 1;
            }
        },
    },
});

app.component('sessionpicker', {
    template: '#session-template',
    setup() {
        const sp = Vue.ref(null);
        return {
            sp
        }
    },
    props: {
        module: {
            type: String,
            default: '',
        }
    },
    data() {
        return {
            selectedDay: "Select a day",
            selectedTime: "",
            timeslots: []
        };
    },
    methods: {
        async fetchTimeslots() {
            try {
                // Replace with your actual API endpoint for moduleItems
                const response = await fetch('http://127.0.0.1:5000/api/v1/timeslots/module', {
                    mode: 'cors',
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        module_code: this.module
                    })
                });
                const timeslotsData = await response.json();
                this.timeslots = timeslotsData;
                console.log(timeslotsData)
            } catch (error) {
                console.error('Error fetching timeslotsData:', error);
            }
        },
    },
    watch: {
        module(newValue, oldValue) {
            this.fetchTimeslots();
        },
    },
    computed: {
        timeOptions() {
            if (this.selectedDay) {
                const selectedDayTimeslots = this.timeslots.find(dayData => dayData.day === this.selectedDay);

                if (selectedDayTimeslots) {
                    return selectedDayTimeslots.timeslots.map(slot => ({
                        value: slot.timeslot_id,
                        label: `${slot.period.start_time}-${slot.period.end_time}`,
                    }));
                }
            }
            return [];
        },
    },
});

app.component('timetracker', {
    template: '#timetracker-template',
    setup() {
        const tt = Vue.ref(null);
        return {
            tt
        }
    },
    props: {
        module: {
            type: String,
            default: '',
        }
    },
    data() {
        return {
            days: ['Select day', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            rows: [],
            initialData: [],
        };
    },
    mounted() {
        if (this.module !== '') {
            this.fetchTimeslots();
        } else {
            this.rows.push({ day: 'Select day', times: '' });
        }

    },
    methods: {
        async fetchTimeslots() {
            try {
                // Replace with your actual API endpoint for moduleItems
                const response = await fetch('http://127.0.0.1:5000/api/v1/timeslots/module', {
                    mode: 'cors',
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        module_code: this.module
                    })
                });
                const timeslotsData = await response.json();

                function transformData(inputData) {
                    // Initialize an empty array to store the transformed data
                    const transformedData = [];

                    // Loop through each day entry in the input data
                    inputData.forEach(dayEntry => {
                        // Initialize an empty array to store timeslot strings for the current day
                        const timeslotStrings = [];

                        function formatTimeSlot(timeSlot) {
                            const startTime = timeSlot.period.start_time.split(':').slice(0, 2).join(':');
                            const endTime = timeSlot.period.end_time.split(':').slice(0, 2).join(':');
                            return `${startTime}-${endTime}`;
                        }
                        // Loop through timeslots for the current day
                        dayEntry.timeslots.forEach(timeslot => {
                            // Extract start and end times from the timeslot
                            const { start_time, end_time } = timeslot.period;

                            // Construct the timeslot string (e.g., "11:00-12:00")
                            const timeslotString = formatTimeSlot(timeslot);

                            // Add the timeslot string to the array
                            timeslotStrings.push(timeslotString);
                        });

                        // Join the timeslot strings with commas to create the final times string
                        const timesString = timeslotStrings.join(', ');

                        // Add the transformed day entry to the result array
                        transformedData.push({
                            day: dayEntry.day,
                            times: timesString,
                        });
                    });

                    return transformedData;
                }

                const formattedTimeslots = transformData(timeslotsData);
                formattedTimeslots.forEach((item) => {
                    this.rows.push({
                        day: item.day,
                        times: item.times
                    });
                });

            } catch (error) {
                console.error('Error fetching timeslotsData:', error);
            }
        },
        addRow() {
            if (this.rows.length < 5) {
                this.rows.push({ day: 'Select day', times: '' });
            }
        },
        removeRow(index) {
            if (index > 0) {
                this.rows.splice(index, 1);
            }
        },
        updateTimes(day, times, index) {
            if (day !== 'Select day') {
                this.rows[index] = { day, times };
            }
        },
        getTimesValidationTitle(index) {
            return this.areTimesValid(index)
                ? 'Looks good! 🤙'
                : 'Its not looking good bruv! 😬 Use: 09:00-10:00, 12:00-13:00, ...';
        },
        areTimesValid(index) {
            const timeFormatRegex = /^(?:[01]\d|2[0-3]):[0-5]\d-(?:[01]\d|2[0-3]):[0-5]\d(?:, ?(?:[01]\d|2[0-3]):[0-5]\d-(?:[01]\d|2[0-3]):[0-5]\d)*$/;
            return timeFormatRegex.test(this.rows[index].times);
        },
        isDayValid(index) {
            return this.rows[index].day !== 'Select day';
        },
        formatTimeslots() {
            let result = [];
            let timeslot;
            for (const { day, times } of this.rows) {
                timeslot = {};
                if (day !== 'Select day') {
                    timeslot['day'] = day;
                    timeslot['times'] = times.split(',').map(slot => slot.trim());
                    result.push(timeslot);
                }
            }
            return result;
        },
        isAllFieldsValid() {
            return this.rows.every(row => {
                const dayIsValid = row.day !== 'Select day';
                const timeFormatRegex = /^(?:[01]\d|2[0-3]):[0-5]\d-(?:[01]\d|2[0-3]):[0-5]\d(?:, ?(?:[01]\d|2[0-3]):[0-5]\d-(?:[01]\d|2[0-3]):[0-5]\d)*$/;
                const timesAreValid = timeFormatRegex.test(row.times);
                return dayIsValid && timesAreValid;
            });
        },
    },
});

const vm = app.mount('#app');