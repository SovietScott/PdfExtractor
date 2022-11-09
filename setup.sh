#!/bin/sh

REQS=$PWD/requirements.txt

activate(){ # Ativa o virtual environment dependendo do OS
   case "$(uname -s)" in
      Linux)
        source .$PWD/venv/bin/activate
      ;;

      CYGWIN*|MINGW32*|MSYS*|MINGW*) # Windows e similares
         . $PWD/venv/Scripts/activate
      ;;
   esac

}

case "$(uname -s)" in # Checa qual é o SO utilizado

   Linux) # Caso Linux
      mkdir -p pdf
      mkdir -p imagens

      virtualenv venv
      activate
   
      if [ -f "$REQS" ]; then
         pip install -r requirements.txt # Instala as dependências do requirements
      else
         pip freeze > requirements.txt
      fi

      pip install --upgrade pip
        
     ;;

    CYGWIN*|MINGW32*|MSYS*|MINGW*) # Caso Windows e similares
      mkdir -p pdf
      mkdir -p imagens

      py -m venv venv
      activate

      if [ -f "$REQS" ]; then
         pip install -r requirements.txt # Instala as dependências do requirements
      else
         pip freeze > requirements.txt
      fi

      py -m pip install --upgrade pip

     ;;

esac



