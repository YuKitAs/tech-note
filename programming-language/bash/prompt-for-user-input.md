# Prompt for User Input

With the help of the Bash build-in `read` command we can display a prompt (with `-p`) and read user input from terminal.

## Use Case 1

```bash
read -p "Username: " username
read -p "Password: " -s password
```

`-s` is used to enable the silent mode, so that the password won't be echoed on the terminal.

## Use Case 2

```bash
while true; do
  read -p "Confirm? (y/n) " answer
  case $answer in
      y|Y)
      # do something
      break;;
      n|N)
      # do something
      break;;
      *)
      echo "Please answer with (y/n)"
      ;;
  esac
done
```

## Reference

* [Catching user input](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_08_02.html) - The Linux Documentation Project
