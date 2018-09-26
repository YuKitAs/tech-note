# Set up Vue Project with Electron

Prerequisite: [npm](https://www.npmjs.com/get-npm), [Yarn](https://yarnpkg.com/en/docs/install#debian-stable), [Vue CLI](https://cli.vuejs.org/)

1. Initialize a Vue.js project:

  ```console
  $ vue init webpack <project-name>
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

4. Edit `package.json` like:


  ```diff
  +  "main": "main.js",
     "scripts": {
       "dev": "webpack-dev-server --inline --progress --config build/webpack.dev.conf.js",
  -    "start": "npm run dev",
  +    "electron": "electron . dev",
       "unit": "cross-env BABEL_ENV=test karma start test/unit/karma.conf.js --single-run",
       "e2e": "node test/e2e/runner.js",
       "test": "npm run unit && npm run e2e",
       "lint": "eslint --ext .js,.vue src test/unit test/e2e/specs",
       "build": "node build/build.js"
     }
  ```

5. Start the test server:

  ```console
  $ yarn dev
  $ yarn electron
  ```
