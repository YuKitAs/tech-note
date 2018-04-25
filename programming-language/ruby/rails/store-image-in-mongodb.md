# Store Image in MongoDB

On the Internet there are some famous gems used to upload files for Rails, like `carrierwave` or `paperclip`. Actually, for images smaller than 10 MB we can store them directy as binary data in MongoDB without installing any gem.

First of all we need an `Image` model with at least a field of type `BSON::Binary`. In this example my simple model looks like this:

```ruby
class Image
  include Mongoid::Document
  field :content, type: BSON::Binary
end
```

Use `curl` to post a local image with `-F` or `--form` option and specify the path starting with an `@` symbol to indicate the rest to be a filename. The whole command will be like:

```console
$ curl -X POST -F 'image=@/home/path/to/image_file.jpg' localhost:3000/images
```

In the way the local image file will be stored as an instance of `ActionDispatch::Http::UploadedFile` (the temporary file can be found in `/tmp`). So we need to convert it to `BSON:Binary` and store it in the `content` field.

With the following code in the controller's `create` action we can save the image into Mongoid:

```ruby
@image = Image.new(content: BSON::Binary.new(params[:image].read))
@image.save! # it's better to use if/else to handle exceptions
```

Make sure we have configured the `routes`. Then we can try to send the `POST` request with the `curl` command mentioned above. On success we will see some logs like:

```console
Processing by ImagesController#create as */*
  Parameters: {"image"=>#<ActionDispatch::Http::UploadedFile:0x00123456789abc @tempfile=#<Tempfile:/tmp/RackMultipart20180425-1234-abcde.jpg>, @original_filename="image_file.jpg", @content_type="image/jpeg", @headers="Content-Disposition: form-data; name=\"image\"; filename=\"image_file.jpg\"\r\nContent-Type: image/jpeg\r\n">}
MONGODB | localhost:27017 | my_database.insert | STARTED | {"insert"=>"images", "ordered"=>true, "documents"=>[{"_id"=>BSON::ObjectId(<id>), "content"=><BSON::Binary:0x12345678 type=generic data=0x12345abc...>}]}
MONGODB | localhost:27017 | my_database.insert | SUCCEEDED | 0.012345678s
Completed 201 Created in 42ms
```

If we check our database, we can see the `content` field of the image includes an encoded string, which is our binary data. To get an image by id we can just send a `GET` request as normal. In the controller, we need to get the data part of the `content`:

```ruby
image_data = @image['content'].data
```

It will be already decoded, and thus can be directly written to a new image file. With the following codes we can check if the output image is identical to the original one:

```ruby
out = File.open('/tmp/out.jpg', 'wb')
out.write(image_data)
out.close
```
