# Upload Image to Server

Tested for Android device only.

## Choose a photo with `react-native-image-picker`

Install [`react-native-image-picker`](https://www.npmjs.com/package/react-native-image-picker) 3.x.

```typescript
import { launchImageLibrary, ImagePickerResponse } from 'react-native-image-picker';
```

Get a photo from library and display:

```typescript
const [photo, setPhoto] = useState<ImagePickerResponse>();

function choosePhoto() {
  const options = {
    mediaType: 'photo' as const
  }

  launchImageLibrary(options, res => {
    if (res.uri) {
      setPhoto(res);
    }
  })
}
```

```typescript
<Button
  title={'Choose photo'}
  onPress={choosePhoto}
/>
{photo && <Image
  source={{ uri: photo.uri }}
  style={{ width: 100, height: 100 }}
/>}
```

## Upload a photo as `multipart/form-data`

Add necessary information as form data for a `photo` field. Don't specify `headers: 'Content-Type: multipart/form-data'` explicitly, otherwise the boundary info will be missing:

```typescript
async function upload(): Promise<any> {
  const data = new FormData();
  data.append('photo', {
    uri: photo!.uri,
    type: photo!.type,
    name: photo!.fileName
  });

  await fetch('http://localhost:3000/upload', {
    method: 'POST',
    body: data,
  }).then(response => {
    if (response.status === 200) {
      Alert.alert('Upload successful.');
      return response.json();
    }
  }).then(body => console.log(body);)
    .catch(error => {
      Alert.alert('Upload failed.');
      console.log(error);
    })
}
```

```typescript
<Button title={'Upload'} onPress={upload} />
```

## Store a photo with `multer`

On the server side, install [`multer`](https://www.npmjs.com/package/multer) (and `@types/multer`) to handle form data.

```typescript
import multer from 'multer';
```

Configure storage path and filename. Read a single file for field `photo` and store the file to disk.

```typescript
const Storage = multer.diskStorage({
  destination(req, file, callback) {
    callback(null, './images')
  },
  // add back file extensions
  filename(req, file, callback) {
    callback(null, `${file.fieldname}_${Date.now()}_${file.originalname}`)
  },
});

const upload = multer({ storage: Storage });

app.post('/upload', upload.single('photo'), (req, res) => {
  console.log(req.file);
  res.send({ 'message': 'Success' });
});
```
