# Set up Vue Project with Electron

Prerequisite: [npm](https://www.npmjs.com/get-npm), [Yarn](https://yarnpkg.com/en/docs/install#debian-stable), [Vue CLI](https://cli.vuejs.org/)

1. Initialize a Vue.js project:

  ```console
  $ vue create <project-name>
  ```

2. In the project root, add `electron` dependency using `yarn`:

  ```console
  $ yarn add -D electron
  ```
  
3. Write a `main.js` as the entry point for Electron:

  ```javascript
  const {app, BrowserWindow} = require('electron')
  const path = require('path')
  const url = require('url')

  function createWindow () {
    mainWindow = new BrowserWindow({width: 800, height: 600})
    mainWindow.loadURL('http://localhost:8080')
    mainWindow.webContents.openDevTools()
  }

  app.on('ready', createWindow)
  ```

4. Edit `package.json`, add two lines like:


  ```diff
  +  "main": "main.js",
     "scripts": {
       "serve": "vue-cli-service serve",
  +    "electron": "electron . dev",
       "build": "vue-cli-service build",
       "lint": "vue-cli-service lint",
       "test:unit": "vue-cli-service test:unit"
     }
  ```

5. Start the test server:

  ```console
  $ yarn serve
  $ yarn electron
  ```
