# Rust Learning Documentation

This Rust learning repository is part of the Life Long Learning Documentation, where the contents would be the same (maybe different content structures), but as in a public repo instead of a private one. 

## Rust Errors

 - In WSL 2.x, when `rustc` got "Permission denied (os error 13)" error. Solved by installing: `sudo apt-get install build-essential`

## git rm cached files

 - reference `.gitignore` for rust projects
 - remove existing files from `.gitignore`:
    ```
    git rm --cached `git ls-files -i -c --exclude-from=.gitignore`
    ```

 
## Rust Fast Check

I don't like "Cheat Sheet" - I am not cheating, I am just having a loose memory sometimes. 

- `cargo doc --open`: generate proj specific documentation.
- 
