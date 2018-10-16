# Use Bash in VS Code Terminal

Powershell is used as the default integrated terminal in Visual Studio Code on Windows. To use Bash, choose `File > Preferences > Settings`, add the following line into the right "User Settings"("Benutzereinstellungen") panel to overwrite the default path of Powershell:

```json
{
  "terminal.integrated.shell.windows": "C:\\path\\to\\bash.exe"
}
```

Save the settings, reopen VS Code and open the terminal, `bash` will be the default shell there.

A quicker way is, click `F1` and search for `Terminal: Select Default Shell`, choose `Git Bash` and reopen VS Code.
