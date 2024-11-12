SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR

REPO_ROOT=$(git rev-parse --show-toplevel)
cd $REPO_ROOT

echo "Running version mismatch example -- this will create new commits in the repository"

rm -rf liba/build libb/build app/build

conan build liba
git commit --allow-empty -m "Dummy commit"
conan build libb
git commit --allow-empty -m "Dummy commit"
conan build app

echo "Versions inside the built binaries:"
./app/build/Release/app

echo "Versions inside conan workspace:"
conan workspace info
