# Interact with Data Model

When the controller action receives the request, it will ask the model to fetch data from the database. The model then returns data to the controller action and the controller action passes the data on to the view. The view renders the page as HTML. Then the controller sends the HTML back to the browser.

## Reading data

1. Create a new model:

  ```console
  $ rails generate model Message
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

  We can add something like `t.text :content` in order to create a text column `content`.

3. Run `rake db:migrate` to update the database with the new data model.

4. Run `rake db:seed` to seed the database with sample data from `db/seeds.rb`.

5. Create a new controller called `Messages`:

  ```console
  $ rails generate controller Messages
  ```

6. Add an `index` action in `app/controllers/messages_controller.rb`:

  ```ruby
  def index
    @messages = Message.all
  end
  ```

  Since `MessageController` inherits `ApplicationController`, the standard controller action `index` is used to list all messages by retrieving all messages from the database and storing them in `@messages`, which will be passed on to the view.

7. Setup `routes.rb`:

  ```ruby
  get '/messages' => 'messages#index'
  ```

8. In `app/views/messages/index.html.erb`, add something like:

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
