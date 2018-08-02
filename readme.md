# tidal-subl

evaluate tidalcycles code from within in sublime text

```haskell
-- works for single lines
d1 $ s "hh bd"

-- and for any number of consecutive lines
d1 $ s "hh bd"
   # crush 4
   # gain 0.8
d2 $ s "cr?*8"
```

based on [vim-tidal](https://github.com/munshkr/vim-tidal). `tidal.sh` has been modified to work with [`stack ghci`](https://www.haskellstack.org/)


## install

- move `tidalcycles.py` to `Packages/User/`
- change variables in `tidal-subl.sh` to your liking


## key bindings

suggestion: `{ "keys": ["alt+enter"], "command": "tidal_eval" }`
