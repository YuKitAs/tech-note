# Read Command Line Arguments

To pass command-line arguments to a bash script using one of the most common formats as follows:

```console
script -u <username> -p <password> -d <data>
```

We can write the script like this:

```shell
usage()
{
  echo "Usage: script -u <username> -p <password> -d <data>" >&2
  echo "       * Option -u, --username:   Username         " >&2
  echo "       * Option -p, --password:   Password         " >&2
  echo "       * Option -d, --data:   Data         " >&2
}

while [[ $# -gt 0 ]]
do
  case $1 in
    -u | --username)
    shift 
    USER="$1"
    ;;
    -p | --password)
    shift
    PASSWORD="$1"
    ;;
    -d | --data)
    shift
    DATA="$1"
    ;;
    *)
    echo "Wrong argument: $1"
    usage
    ;;
  esac
  shift
done

echo USER=$USER
echo PASSWORD=$PASSWORD
echo DATA=$DATA
```
