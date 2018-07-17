# Use Bash in VS Code Terminal

Powershell is used as the default integrated terminal in Visual Studio Code on Windows. To use Bash, open "User Settings"("Benutzereinstellungen"), add the following line into the right panel to overwrite the default path of Powershell:

```json
{
  "terminal.integrated.shell.windows": "C:\\path\\to\\bash.exe"
}
```

Save the settings, open the terminal, click the `+` button or use `Ctrl + Shift + Ö` to open a terminal, then choose `bash` from the dropdown menu.
