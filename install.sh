#!/bin/bash
set -e
ENV=${1:-numopt}
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

function check_conda {
  set +e
  conda=$(which conda)
  set -e
  if [[ -z "$conda" ]]; then
    echo "Didn't found conda! Please install miniconda first."
    exit 1
  fi
}

function make_env {
  conda config --set always_yes true
  if conda env list | awk {'print $1'} | grep -q $ENV; then
      echo "Found old enviroment! It will be removed and a clean new one will be installed."
      conda remove --name "$ENV" --all --quiet
  fi
  echo "Creating Enviroment: $ENV"
  conda create python=3.6 --name $ENV --quiet
  source activate $ENV
  pip install -e $DIR
  source deactivate

}

echo "Install numerical Optimization"
check_conda
make_env
