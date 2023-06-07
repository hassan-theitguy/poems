if [ -z "$1" ] || [ "$1" != "prod" ]; then
  export NODE_ENV_POEMS="development"
else
  export NODE_ENV_POEMS="production"
fi

rm -rf ../docs

npx @11ty/eleventy

pf_dir="/data/data/com.termux/files/home/.cargo/bin"

if [[ ":$PATH:" != *":$pf_dir:"* ]]; then
    echo "Pagefind dir is not in PATH. Adding it."
    export PATH="$pf_dir:$PATH"
else
    echo "Pagefind dir is already in PATH."
fi

pagefind --source "../docs/poems" --glob "**/*.*"

touch ../docs/.nojekyll

echo $NODE_ENV_POEMS
echo $1

#Need to source this script to preserve variable for launch.sh script
