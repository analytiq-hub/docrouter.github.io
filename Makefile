.PHONY: install serve drafts build clean

install:
	bundle install

# Development target - Jekyll server only (Tailwind via CDN)
serve:
	@echo "Starting development environment..."
	@echo "Starting Jekyll server..."
	bundle exec jekyll serve

# Development server that also renders posts in _drafts/
drafts:
	@echo "Starting Jekyll server with drafts..."
	bundle exec jekyll serve --drafts

# Build for production
build:
	@echo "Building Jekyll site..."
	bundle exec jekyll build

# Clean generated files
clean:
	bundle exec jekyll clean