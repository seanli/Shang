DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

lessc $DIR/shang/assets/less/shang.less > $DIR/shang/assets/css/shang.css
