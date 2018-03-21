# Interact with Data Model

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

4. Run `rake db:seed` to seed the database with sample data from `db/seeds.rb`.

5. Create a new controller called `Messages` with an `index` action:

  ```console
  $ rails generate controller Messages index
  ```

6. In `app/controllers/messages_controller.rb`, implement the `index` method as follows:

  ```ruby
  def index
    @messages = Message.all
  end
  ```

  Since `MessageController` inherits `ApplicationController`, the [standard controller action](https://www.codecademy.com/articles/standard-controller-actions) `index` is used to list all messages by retrieving all messages from the database and storing them in `@messages`, which will be passed on to the view.

7. In `config/routes.rb`, Rails has created a route `get 'messages/index'`. We could also modify it like:

  ```ruby
  get 'messages' => 'messages#index'
  ```

8. In `app/views/messages/index.html.erb`, add HTML elements for message contents and timestamps with [ERB templating language](http://ruby-doc.org/stdlib-2.5.0/libdoc/erb/rdoc/ERB.html) like:

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

## Creating data

### Implementation example

1. Create a route that maps request `GET /messages/new` to `Messages` controller's `new` action, and request `POST messages` to `Messages` controller's `create` action:

  ```ruby
  get 'messages/new' => 'messages#new'
  post 'messages' => 'messages#create'
  ```

2. Add `new` and `create` actions in `Message` controller:

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

3.  Add a private method `message_params`:

  ```ruby
  private
    def message_params
      params.require(:message).permit(:content)
    end
  ```
  
  The `params` method returns an `ActionController::Parameters` object.

4. In the view page `app/views/new.html.erb`, add the following content to display a form for new messages with a submit button:

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

5. In `index.html.erb`, use `link_to` to create a link to `/messages/new`:

```erb
<%= link_to 'New Message', "messages/new" %>
```
