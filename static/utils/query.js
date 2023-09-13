let tags = []

function handleMultiSelectSearch (text, dropdown_items, limit=-1) {
    console.log('search limit | ', limit);
    const content = fetchContent('http://127.0.0.1:5000/api/v1/searchfield-config',JSON.stringify({value : text, dropdown_items : dropdown_items, tags : tags, limit : limit}));
    content.then((c) => {
        renderHTML('dropdown-items',c);
    });
}

async function handleDropdownItemClick (item, limit=-1) {
    console.log(limit);
    if (!tags.includes(item)) {
        tags.push(item)
    } else {
        tags = tags.filter((val) => val!==item);
    }
    console.log(tags);

    dropdown_items = await fetch('http://127.0.0.1:5000/dropdown-items',{ 
        method : "GET",mode: "no-cors", cache: "no-cache",
        headers: {
        "Content-Type": "application/json",
        }}).then((result) => result.json());

    const content = fetchContent('http://127.0.0.1:5000/api/v1/dropdown-config',JSON.stringify({value : item, dropdown_items : dropdown_items, tags : tags, limit : limit}));
    content.then((c) => {
        renderHTML('multiselect',c);
    });
}

/**
 * Debounces input field/element by invoking callback function after user stops typing.
 * @param {string} id - an identifier for target element
 * @param {function} cb - a callback function to run after timeout
 */
async function debounceInput(id, limit=-1) {
    let timeoutId;
    const waitTime = 800;

    const input = document.getElementById(id);
    dropdown_items = await fetch('http://127.0.0.1:5000/api/v1/dropdown-items',{ 
        method : "GET",mode: "no-cors", cache: "no-cache",
        headers: {
        "Content-Type": "application/json",
        }}).then((result) => result.json());

        input.addEventListener('keyup', (e) => {
        const text = e.currentTarget.value;

        clearTimeout(timeoutId);

        timeoutId = setTimeout(() => {
            handleMultiSelectSearch(text, dropdown_items, limit);
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