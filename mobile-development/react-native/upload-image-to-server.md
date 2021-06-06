# Upload Image to Server

Tested on Android device only.

## Single photo with `react-native-image-picker`

Install [`react-native-image-picker`](https://www.npmjs.com/package/react-native-image-picker) 3.x and import `launchImageLibrary`:

```typescript
import { launchImageLibrary, ImagePickerResponse } from 'react-native-image-picker';
```

### Choose a photo

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
  });
}
```

### Upload a photo

Add necessary information `uri`, `type` and `name` as form data for a `photo` field. Don't specify `headers: 'Content-Type: multipart/form-data'` explicitly, otherwise the boundary info will be missing:

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
  }).then(body => console.log(body))
    .catch(error => {
      Alert.alert('Upload failed.');
      console.log(error);
    })
}
```

### UI components

```typescript
<Button
  title={'Choose photo'}
  onPress={choosePhoto}
/>
{photo && <Image
  source={{ uri: photo.uri }}
  style={{ width: 100, height: 100 }}
/>}
<Button title={'Upload'} onPress={upload} />
```

## Multiple photos and videos with `react-native-image-crop-picker`

Install [`react-native-image-crop-picker`](https://www.npmjs.com/package/react-native-image-picker) and import `ImagePicker`:

```typescript
import ImagePicker, { ImageOrVideo } from 'react-native-image-crop-picker';
```

### Choose multiple photos/videos

```typescript
const [filesToUpload, setFilesToUpload] = useState<ImageOrVideo[]>([]);

function choosePhoto() {
  ImagePicker.openPicker({
    multiple: true
  }).then(images => {
    setFilesToUpload(images);
  });
}
```

### Upload multiple photos/videos

```typescript
async function upload(): Promise<any> {
  const data = new FormData();
  filesToUpload.forEach(item => {
    data.append('photo', {
      uri: item.path,
      type: item.mime,
      name: item.path.substring(item.path.lastIndexOf('/') + 1)
    });
  });
  // the rest is the same
}  
```

## Store file(s) with `multer`

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
```

Single file:

```typescript
app.post('/upload', upload.single('photo'), (req, res) => {
  console.log(req.file);
  res.send({ 'message': 'Success' });
});
```

Multiple files (with count limit):

```typescript
app.post('/upload', upload.array('photo', 10), (req, res) => {
  console.log(req.files);
  res.send({ 'message': 'Success' });
});
```
