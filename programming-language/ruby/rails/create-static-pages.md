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
  $ rails generate controller Pages [action]
  ```

  Some new files related to `Pages` controller will be created by Rails. If we apend an action e.g. `home` when we generate the controller, then Rails will also create a route `get 'pages/home'` (see next step).
  
  The most important file is `pages_controller.rb` in `app/controllers` with the following content:

  ```ruby
  class PagesController < ApplicationController
  end
  ```

  We can add different action methods into this controller, e.g. a `home` method:

  ```ruby
  def home
  end
  ```

4. In `config/routes.rb`, we tell the router how to match requests to controller actions. As mentioned above, Rails would have created a route `get 'pages/home'`, which means using URL `/pages/home` will hit `Pages` controller's `home` action. If we want to use an arbitrary request string, we can modify the route like:

  ```ruby
  get 'hello' => 'pages#home'
  ```
  
  Moreover, we can also specify the root of the application as the `home` page (see next step) by adding `root 'pages#home'`.

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

6. Run `rails server` and open `localhost:3000/hello` in browser to check the `home` page that we created. If we have specified the root, just use `localhost:3000` to get the same page.
