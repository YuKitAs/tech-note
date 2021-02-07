# Auto Sort Imports for Typescript Projects

In `Preferences` > `Text Editor` > `settings.json`, add the following:

```json
"[typescript]": {
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
},
"[typescriptreact]": {
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

The the imports will be sorted alphabetically on save.
