// Import the SDK
// (1) Import dropbox and instantiate a dropbox (dbx) class


import { Dropbox } from 'dropbox'

const dbx = new Dropbox({
    accessToken: 'sl.BH2GE_Oxvi-KSF4qkk5DB3qpfA7Q-5XWh-apNVAdfOllLc9Q2Uu1v-MBc9jGSIpURXuTSc7tRORZwVJOVQTU7Cs6DlGaGcUdvPfVA81K91cVaNd0p9DYsmM8-iHt-boRVvEK5oY',
    fetch 
})

//declare an element to interact with 

const fileListElement = document.querySelector('.js-file-list')
const loadingElem = document.querySelector('js-loading')
const rootPathForm = document.querySelector('js-root-path__form')
const rootPathInput = document.querySelector('.js-root-path__input')

rootPathFormaddEventListener('submit', e=> {
    e.preventDefault();
    state.rootPath = rootPathInput.value === '/' ? '' : rootPathInput.value.toLowerCase()
    state.files = []
    loadingElem.classList.remove('hidden')
    init()
})

const state = {
    files: [],
    rootPath: ''
}
// init function calling our update files, which calls our render files function, which renders to the dom  
const init = async () => {
    const res = await dbx.filesFolder({
        path: state.rootPath,
        limit: 20
    })
    updateFiles(res.entries)
    if (res.has_more) {
        loadingElem.classList.remove('hidden')
        await getMoreFiles(res.cursor, more => updateFiles(more.entries))
        loadingElem.classList.add('hidden')
    } else {
        loadingElem.classList.add('hidden')
    }
    
}
// methods available in the dbx class accessible here: https://dropbox.github.io/dropbox-sdk-js/Dropbox.html
// first method 

// dbx.filesListFolder({
//     // route of our app folder not dropbox account 
//     path: ''
// }).then(res => console.log(res))

// declare an update files function IOT take files and update the state accordingly and update with the new ones 
const updateFiles = files => {
    state.files = [...state.files, ...files]
    renderFiles()
    getThumbnails(files)
}

const getMoreFiles = async (cursor, cb) => {
    const res = dbx.filesListFolderContinue({cursor})
    if (cb) cb(res)
    if (res.has_more) {
       await getMoreFiles(res.cursor, cb)
    }
}

const renderFiles = () => {
    filesListElem.innerHTML = state.files.sort((a,b) => {
        // sort alphabetically folders first w/ (||) operand
        // are either one of these a folder if so, check if they are the same, 
        // if both folders or files we dont need to do anything with them except organize them alphabetically,
        // but if one of them is a folder and one of them is a file, 
        // check which one return -1 to say it should come first, positive 1 to returnn second
        if ((a['tag'] === 'folder' || b['.tag'] === 'folder') 
        && !(a['.tag'] === b['.tag'])) { 
            return a['.tag'] === 'folder' ? -1 : 1
        } else {
            return a.name.toLowerCase() < b.name.toLowerCase() ? -1 : 1
        }
    }).map(file => {
        const type = file['.tag']
        let thumbnail
        if (type === 'file') {
           // ternary function ifSomething ? doSomething : doSomethingElse
           thumbnail = file.thumbnail
           ? `data:image/jpeg;base64, ${file.thumbnail}`
           //default thumbnail: `data:image/svg+xml;base64,
           : `https://cdn.pixabay.com/photo/2021/12/11/15/06/northern-lights-6862969_960_720.jpg`
        } else {
            thumbnail = `https://cdn.pixabay.com/photo/2021/12/11/15/06/northern-lights-6862969_960_720.jpg`
        }
        return `
        <li class= "dbx-list-item ${type}">
        <img class= "dbx-thumb" src="${thumbnail}">
        ${file.name}
        </li> 
        `              
    }).join('')
}

const getThumbnails = async files => {
    const paths = files.filter(file => file ['.tag'] == 'file')
    .map(file => ({
        path:file_lower,
        size: 'w32h32'
    }))
    const res = await dbx.filesGetThumbnailBatch({
        entries: paths
    })
    // make a copy of state.files
    const newStateFiles = [...state.files]
    // loop through the file objects returned from the dbx 
    res.entries.forEach(file => { 
        // figure out the index of the file we need to update
        let indexToUpdate = state.files.findIndex(
            stateFile => file.metadata.path_lower === stateFile.path_lower
        )
        //put a .thumbnail property on the corresponding file 
        newStateFiles[indexToUpdate].thumbnail = file.thumbnail
    })
    state.files = newStateFiles
    renderFiles()
    
}
    

init()