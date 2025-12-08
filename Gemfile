source "https://rubygems.org"

# GitHub Pages gem includes Jekyll and all required plugins at compatible versions
gem "github-pages", group: :jekyll_plugins

# Windows and JRuby do not include zoneinfo files, so bundle the tzinfo-data gem
platforms :mswin, :mingw, :x64_mingw, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1", platforms: [:mswin, :mingw, :x64_mingw]

# Lock to webrick for Ruby 3.0+ compatibility
gem "webrick", "~> 1.8"
