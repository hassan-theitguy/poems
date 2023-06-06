if [ -z "$1" ] || [ "$1" != "prod" ]; then
  export NODE_ENV_POEMS="development"
else
  export NODE_ENV_POEMS="production"
fi

npx @11ty/eleventy

echo $NODE_ENV_POEMS
echo $1

#Need to source this script to preserve variable for launch.sh script
