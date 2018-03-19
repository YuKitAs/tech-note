# Create Static Pages

This is a tutorial for creating a static page in Ruby on Rails without using models.

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

  Some new files related to `Pages` controller will be created. The most important file is `pages_controller.rb` in `app/controllers` with the following content:

  ```ruby
  class PagesController < ApplicationController
  end
  ```

  We can add different action methods into this controller, e.g. a `home` method:

  ```ruby
  def home
  end
  ```

4. In `configs/routes.rb` we can make the router match to controller actions. For example, adding the following line means, the router should match `GET /hello` request to `Pages` controller's `home` action:

  ```ruby
  get 'hello' => 'pages#home'
  ```

5. Next, we create a file called `home.html.erb` under `app/views/pages` with some HTML content like:

  ```html
  <div class="main">Hello world!</div>
  ```

6. A SCSS file for `Pages` controller is created in `app/assets/stylesheets/pages.scss`, so we can customize the styles here:

 ```css
 .main {
   text-align: center;
   font-size: 30px;
 }
 ```

6. Run `rails server` and open `localhost:3000/hello` in browser to check the `home` page we just created. 
