run:
	bundle exec jekyll serve

break_lock:
	bundle config set --local path 'vendor/bundle'	

build:
	bundle install
