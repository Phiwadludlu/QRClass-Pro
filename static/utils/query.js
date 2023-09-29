let qualification_tags = []
let module_tags = []

function handleMultiselectSearch(text, dropdown_items, limit = -1) {
    let item_type;
    try {
        item_type = dropdown_items[0].type;
    } catch (e) {
        item_type = '';
    }

    let tags = getTagList(item_type);

    const content = fetchContent('http://127.0.0.1:5000/api/v1/config/multiselect/search', JSON.stringify({ value: text, dropdown_items: dropdown_items, tags: tags, limit: limit }));
    content.then((c) => {
        renderHTML('dropdown-items', c);
    });
}

async function handleMultiselectDropdown(item, type, limit = -1) {
    const multiselect = document.getElementById(`multiselect-${type}`);
    const new_tags = handleTags(item, type);
    multiselect.dataset.currentLength = new_tags.length;
    console.log(new_tags);

    const qualification_tags_length = qualification_tags.length;
    const module_tags_length = module_tags.length;

    dropdown_items = await fetch(`http://127.0.0.1:5000/api/v1/${type}/all`, {
        method: "GET", mode: "no-cors", cache: "no-cache",
        headers: {
            "Content-Type": "application/json",
        }
    }).then((result) => result.json());

    const content = fetchContent('http://127.0.0.1:5000/api/v1/config/multiselect/dropdown', JSON.stringify({ value: item, dropdown_items: dropdown_items, tags: new_tags, limit: limit, qualification_tags_length, module_tags_length }));
    content.then((c) => {
        renderHTML(`multiselect-${type}`, c);
    });
}

/**
 * Debounces input field/element by invoking callback function after user stops typing.
 * @param {string} id - an identifier for target element
 * @param {function} cb - a callback function to run after timeout
 */
async function debounceInput(id, type, limit = -1) {
    let timeoutId;
    const waitTime = 800;

    const input = document.getElementById(id);
    dropdown_items = await fetch(`http://127.0.0.1:5000/api/v1/${type}/all`, {
        method: "GET", mode: "no-cors", cache: "no-cache",
        headers: {
            "Content-Type": "application/json",
        }
    }).then((result) => result.json());

    input.addEventListener('keyup', (e) => {
        const text = e.currentTarget.value;

        clearTimeout(timeoutId);

        timeoutId = setTimeout(() => {
            handleMultiselectSearch(text, dropdown_items, limit);
        }, waitTime);
    });
}

function renderHTML(dest_id, data) {
    const renderOn = document.getElementById(dest_id);
    renderOn.innerHTML = data;
}

const fetchContent = async (url, data) => {
    const res = await fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "no-cors", // no-cors, *cors, same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        //credentials: "same-origin", // include, *same-origin, omit
        headers: {
            "Content-Type": "application/json",
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        //redirect: "follow", // manual, *follow, error
        //referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data), // body data type must match "Content-Type" header
    })
        .then((result) => {
            return result.text();
        })
        .catch((e) => {
            console.log(e);
        });

    return res;
}

function handleTags(value, type) {
    let tags = tagsByType(type);

    if (!tags.includes(value)) {
        tags.push(value);
    } else {
        tags = tags.filter((val) => val !== value);
    }

    if (type === 'qualification') {
        qualification_tags = tags;
    } else if (type === 'module') {
        module_tags = tags;
    }

    return tags;
}

function tagsByType(type){
    return (type!=='qualification' && type!=='module') ? [] : 
        ((type === 'qualification') ? qualification_tags : module_tags);
}