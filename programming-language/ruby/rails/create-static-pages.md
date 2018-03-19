# Create Static Pages

1. Create a new Ruby on Rails app:

  ```console
  $ rails new hello-world
  ```

  A new project called `hello-world` will be created.

2. In the project root, run `bundle install` to install all the gems.

3. Create a controller called `Pages`:

  ```console
  $ rails generate controller Pages
  ```

  A new file called `pages_controller.rb` will be generated under `hello-world/app/controllers` with the following definition:

  ```ruby
  class PagesController < ApplicationController
  end
  ```

  We can add different action methods into this controller, e.g. a `home` method:

  ```ruby
  def home
  end
  ```

4. In `configs/routes.rb` we can make the router match to controller actions. For example, adding the following line means, the router should match `GET /hello` request to `pages` controller's `home` action:

  ```ruby
  get 'hello' => 'pages#home'
  ```

5. Next, we create a file called `home.html.erb` under `app/views/pages` with some HTML content like:

  ```html
  <div class="main">
    <h1>Hello world!</h1>
  </div>
  ```

  The CSS/SCSS files are in `app/assets/stylesheets`.

6. Run `rails server` and open `localhost:3000/hello` in browser to check the `home` page we just created. 
