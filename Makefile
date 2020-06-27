# https://research.mach1.tech
s3_bucket_name = mach1-research-public

# getting OS type
ifeq ($(OS),Windows_NT)
	detected_OS := Windows
else
	detected_OS := $(shell uname)
endif

# Commands for generating + deploying front-end
build: FORCE
	# generate static site
	hugo -D
deploy: build/
	# deploys build to public AWS bucket
	# NOTE: relies on `mach1` keys in `~/.aws/credentials`
	cd public/
	aws s3 sync public/ s3://$(s3_bucket_name) --content-type text/html --cache-control no-cache --acl public-read --metadata-directive REPLACE --exclude "*" --include "*.html" --profile mach1
	aws s3 sync public/ s3://$(s3_bucket_name) --content-type text/plain --cache-control no-cache --acl public-read --metadata-directive REPLACE --exclude "*" --include "*.txt" --profile mach1
	aws s3 sync public/ s3://$(s3_bucket_name) --content-type text/css --cache-control no-cache --acl public-read --metadata-directive REPLACE --exclude "*" --include "*.css" --profile mach1
	aws s3 sync public/ s3://$(s3_bucket_name) --content-type application/xhtml+xml --cache-control no-cache --acl public-read --metadata-directive REPLACE --exclude "*" --include "*.xml" --profile mach1
	aws s3 sync public/ s3://$(s3_bucket_name) --content-type image/svg+xml --cache-control no-cache --acl public-read --metadata-directive REPLACE --exclude "*" --include "*.svg" --profile mach1
	aws s3 sync public/ s3://$(s3_bucket_name) --content-type audio/aiff --cache-control no-cache --acl public-read --metadata-directive REPLACE --exclude "*" --include "*.aif" --include "*.aiff" --profile mach1
	aws s3 sync public/ s3://$(s3_bucket_name) --content-type audio/mpeg --cache-control no-cache --acl public-read --metadata-directive REPLACE --exclude "*" --include "*.mp3" --profile mach1
	aws s3 sync public/ s3://$(s3_bucket_name) --content-type audio/wav --cache-control no-cache --acl public-read --metadata-directive REPLACE --exclude "*" --include "*.wav" --profile mach1
	aws s3 sync public/ s3://$(s3_bucket_name) --cache-control no-cache --acl public-read --metadata-directive REPLACE --exclude "*.html" --exclude "*.txt" --exclude "*.css" --exclude "*.xml" --exclude "*.svg" --profile mach1

clean:
	# remove generated static site
	rm -fr public/
local:
	hugo server -D

FORCE:
