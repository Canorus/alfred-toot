# alfred-toot

### Send toot from Alfred

- Input instance address, key code, re-run the workflow and you're good to go.
- Login credentials are stored in workflow environmental variables that won't be exported elsewhere.
- Set custom hotkey.
- Single account only. It's for quick compose after all.
- **Requires registered version of Alfred**
- All versions are at [Releases page](https://github.com/Canorus/alfred-toot/releases)

### Content Warning

- append `!cw:` after your toot and continue with your spoiler message. 
- ~~should be placed after your toot because I can't decide where spoiler message ends.~~ no longer necessary as of 1.0-3

### Visibility (1.0-3)

- can modify visibility
- append visibility option after `!visib:` or `!visibility:` 
- visibility option has: `public`, `unlisted`, `private`, `direct`. For detailed information, see [official documentation](https://github.com/tootsuite/documentation/blob/master/Using-Mastodon/User-guide.md#toot-privacy)

### Clipboard image (1.0-4)

- Append image from clipboard, by adding `!clipboard:` of `!cb:`

------

### Todo

- [x] ~~Contents warning message~~
- [ ] multiple accounts
- [x] ~~visibility~~
- [ ] line break
- [x] Append single image from clipboard

------

### Changelog

- 1.0-1
  - added Content Warning
  - added workflow icon
- 1.0-3
  - added visibility option on sending toot
- 1.0-4
  - added attching single image from clipboard

------

As always, any pull requests or ideas will be appreciated. If you have problem, please contact me on [twingyeo](https://twingyeo.kr/@canor) or [cmx](https://cmx.im/@canor).
