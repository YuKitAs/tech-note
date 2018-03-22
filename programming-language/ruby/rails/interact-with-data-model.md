# Interact with Data Model

Table of Contents

* [Creating data](#creating-data)
* [Reading data](#reading-data)
  * [Listing all messages](#listing-all-messages)
  * [Showing a message](#showing-a-message)
* [Updating data](#updating-data)
* [Deleting data](#deleting-data)

## Creating data

1. Create a new model:

  ```console
  $ rails generate model Message [attributes]
  ```

  A model file called `message.rb` will be created in `app/models` which represents a table in the database.

2. In the migration file in `db/migrate` prefixed by a creation timestamp, we can see a method called `create_table`. As the name indicates, it's used to create a new table in the database:

  ```ruby
  class CreateMessages < ActiveRecord::Migration
    def change
      create_table :messages do |t|
        t.timestamps
      end
    end
  end
  ```

  `t.timestamps` is a Rails command that creates two default columns `created_at` and `updated_at` in the `message` table.

  We can add `t.text :content` in order to create a text column `content`. It can also be done in the last step by appending `content:text`.

3. Run `rake db:migrate` to update the database with the new data model (the `change` method will be called).

4. Create a new controller called `Messages`:

  ```console
  $ rails generate controller Messages
  ``` 

5. We don't need to create a route that maps request `GET /messages/new` to `Messages` controller's `new` action. Instead, we can add a `messages` resource in `config/routes.rb` as follows:

  ```ruby
  resources :messages
  ```
  
  Now, if we run `rails routes`, we'll see that Rails has automatically defined routes for all the standard RESTful actions.

6. Add `new` and `create` actions in `Message` controller:

  ```ruby
  def new
    @message = Message.new
  end

  def create
    @message = Message.new(message_params)
    # save the Message model to database
    if @message.save
      redirect_to '/messages'
    else
      render 'new'
    end
  end
  ```

7. Implement the private method `message_params`:

  ```ruby
  private
    # this method is made private to make sure it can't be called outside its intended context
    def message_params
      # allow and require the content parameter for valid use of creating message
      params.require(:message).permit(:content)
    end
  ```
  
  The `params` method returns an `ActionController::Parameters` object.

8. Create a view page `app/views/messages/new.html.erb`, add the following content to display a form for new messages, which consists of a text area and a submit button labeled "Create":

  ```erb
  <%= form_with(scope: @message, url: messages_path, local: true) do |f| %>  
    <div class="field">
      <%= f.label :message %><br>
      <%= f.text_area :content %>
    </div>
    <div class="actions">
      <%= f.submit "Create" %>
    </div>
  <% end %>
  ```
  The `messages_path` helper passed to `url` tells Rails to point the form to the URI Pattern associated with the `messages` prefix, and the form will send a POST request to that route by default.

9. In `index.html.erb`, use `link_to` to create a link to `/messages/new`:

  ```erb
  <%= link_to 'New Message', "messages/new" %>
  ```

## Reading data

### Steps

1. User input a URL in the browser

2. By entering Enter, the browser sends a `GET` request to server

3. The router maps the URL to the corresponding controller action to handle the request

4. The controller action receives the request and asks the model to fetch data from the database

5. The model returns data to the controller action

6. The controller action passes the data on to the view

7. The view renders the page as HTML

8. The controller sends the HTML back to the browser

### Listing all messages

1. Run `rake db:seed` to seed the database with sample data from `db/seeds.rb`.

2. In `messages_controller.rb`, add an `index` action and implement it as follows:

  ```ruby
  def index
    @messages = Message.all
  end
  ```

  Since `MessageController` inherits `ApplicationController`, the [standard controller action](https://www.codecademy.com/articles/standard-controller-actions) `index` is used to list all messages by retrieving all messages from the database and storing them in `@messages`, which will be passed on to the view.

3. In `app/views/messages/index.html.erb`, use [ERB templating language](http://ruby-doc.org/stdlib-2.5.0/libdoc/erb/rdoc/ERB.html) to display the contents and timestamp for each message:

  ```erb
  <div class="messages">
    <div class="container">
      <% @messages.each do |message| %>
      <div class="message">
        <p class="content"><%= message.content %></p>
        <p class="time"><%= message.created_at %></p>
      </div>
      <% end %>
    </div>
  </div>
  ```

### Showing a message

We may want to navigate to a page with URL like `/messages/<id>` displaying a specific message, then we need to find the message by its id.

1. Add a `show` action in `messages_controller.rb`:

  ```ruby
  def show
    @message = Message.find(params[:id])
  end
  ```

2. Create a new file `app/views/messages/show.html.erb` and add something like:

  ```ruby
  <div class="message">
    <p class="content"><%= @message.content %></p>
    <p class="time"><%= @message.created_at %></p>
  </div>

  <%= link_to 'Back', messages_path %>
  ```

3. Add a link to `show` page in `app/views/messages/index.html.erb` after each message:

  ```erb
  <%= link_to 'Show', message_path(message) %>
  ```

## Updating data

1. Add an `edit` action into `messages_controller.rb`, by editing we also need to find the message by its id just like `show` action:

  ```ruby
  def edit
    @message = Message.find(params[:id])
  end
  ```
  
2. Create a `edit` page called `app/views/messages/edit.html.erb` with contents like:

  ```erb
  <h1>Edit message</h1>

  <%= form_with(model: @message, local: true) do |form| %>
    <div class="field">
      <%= f.label :message %><br>
      <%= f.text_area :content %>
    </div>
    <div class="actions">
      <%= f.submit "Create" %>
    </div>
  <% end %>
  ```

  We can see the `edit` page and the `new` page share the same code for displaying the form. But here we pass `model: @message` to `form_with`, it would cause the helper to fill in the form with the fields of the `message` object. 

  Actually, we can use [partials](http://guides.rubyonrails.org/layouts_and_rendering.html#using-partials) to clean up the duplication by creating a new file `app/views/messages/_form.html.erb` and replace the duplicated part with `<%= render 'form' %>`.

3. Add an `update` action into `messages_controller.rb`:

  ```ruby
  def update
    @message = Message.find(params[:id])

    if @message.update(message_params)
      redirect_to @message
    else
      render 'edit'
    end
  end
  ```

4. Add a link `<%= link_to 'Edit', edit_message_path(message) %>` in `index.html.erb` and `<%= link_to 'Edit', edit_message_path(@message) %>` in `show.html.erb`.

## Deleting data

1. Add a `destroy` action:

  ```ruby
  def destroy
    @message = Message.find(params[:id])
    @message.destroy

    redirect_to messages_path
  end
  ```

2. Add a link in `index.html.erb`:

  ```erb
  <%= link_to 'Destroy', messages_path(message), method: :delete, data: { confirm: 'Are you sure?' } %>
  ```
  
  By this way Rails will prompt a confirm dialog and then submit the link with method `delete`. This is done via the JavaScript file `rails-ujs` which is automatically included in `app/views/layouts/application.html.erb`. 
  
Conventionally, the order of the actions in `messages_controller.rb` defined above would be like this:

```ruby
def index; end
def show; end
def new; end
def edit; end
def create; end
def update; end
def destroy; end
```

