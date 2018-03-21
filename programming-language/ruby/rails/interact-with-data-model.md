# Interact with Data Model

Table of Contents

* [Creating data](#creating-data)
* [Reading data](#reading-data)
  * [Listing all messages](#listing-all-messages)
  * [Showing a message](#showing-a-message)
* Updating data
* Deleting data

## Creating data

### Implementation example

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

5. Create a route in `config/routes.rb` that maps request `GET /messages/new` to `Messages` controller's `new` action, and request `POST messages` to `Messages` controller's `create` action:

  ```ruby
  get 'messages/new' => 'messages#new'
  post 'messages' => 'messages#create'
  ```

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
<%= form_for(@message) do |f| %>  
  <div class="field">
    <%= f.label :message %><br>
    <%= f.text_area :content %>
  </div>
  <div class="actions">
    <%= f.submit "Create" %>
  </div>
<% end %>
```

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

### Implementation example

#### Listing all messages

1. Run `rake db:seed` to seed the database with sample data from `db/seeds.rb`.

2. In `messages_controller.rb`, add an `index` action and implement it as follows:

  ```ruby
  def index
    @messages = Message.all
  end
  ```

  Since `MessageController` inherits `ApplicationController`, the [standard controller action](https://www.codecademy.com/articles/standard-controller-actions) `index` is used to list all messages by retrieving all messages from the database and storing them in `@messages`, which will be passed on to the view.

3. In `routes.rb`, add a new route for `Messages` controller's `index` action:

  ```ruby
  get 'messages' => 'messages#index'
  ```

4. In `app/views/messages/index.html.erb`, use [ERB templating language](http://ruby-doc.org/stdlib-2.5.0/libdoc/erb/rdoc/ERB.html) to display the contents and timestamp for each message:

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

#### Showing a message

We may want to navigate to a page like `/messages/<id>` displaying a specific message, then we need to find the message by its id.

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
```

### Updating data


### Deleting data
