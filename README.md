# Conan workspace test

The commands here assume WSL/Linux, but they might work in Git Bash in Windows, too.

## Version diff

When using dynamic versioning, workspace editables becomes a bit weird. The static versions of
editables in `conanws.yml` can have a mismatch between the actual versions of the packages, deduced
by dunamai in the repos (pretend that `liba`, `libb` and `app` are different repos here).

When running `./example_scripts/version_mismatch.sh`, two empty commits will be created in this
repo. The steps are done in the following order:

* `conan build liba`
* `git commit --allow-empty -m "Dummy commit"`
* `conan build libb`
* `git commit --allow-empty -m "Dummy commit"`
* `conan build app`

Now, all three "sub-repos" have different versions; this can be verified by running
`./app/build/Release/app`. However, the versions are static in `conanws.yml`, and are not matching
the actual versions. In the current `app/conanfile.py` it does not strictly matter since we are
picking any package anyway, but there could be situations where we either pick something that is not
the editable workspace versions if there is a different version in the cache which is later.

To avoid having to update `conanws.yml` all the time, it would be beneficial to be able to configure
`conanws.yml` to have something along the lines of `liba/*` instead of `liba/0.0.1-pre.9+ac72de1`. I
imagine this would have one of two behaviors:

* When running `conan workspace` commands, we dynamically run `set_version` or get the `version`
  attribute for all packages with `/*` in `conanws.yml`, add that as editable for the current
  command, and at the end of the current command remove it from the editable list in the conan
  cache.
* When running `conan workspace` commands, whatever the version of `liba` is, we override every
  single dependency/requires towards `liba` to what we have in our conan workspace.

I guess these do not necessarily need to be mutually exclusive, and the second one could perhaps be
toggled with a flag for each package in the workspace?
