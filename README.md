# alfred-toot

Original repository is removed because I found out a file contains my login credential.

### Send toot from Alfred

- Input instance address, key code, re-run the workflow and you're good to go.
- Login credentials are stored in workflow environmental variables that won't be exported elsewhere.
- Set custom hotkey.
- Single account only. It's for quick compose after all.
- **Requires registered version of Alfred**
- All versions are at [Releases page](https://github.com/Canorus/alfred-toot/releases)

### Content Warning

- append `!cw:` after your toot and continue with your spoiler message. 

### Visibility (1.0-3)

- can modify visibility
- append visibility option after `!visib:` or `!visibility:` 
- visibility option has: `public`, `unlisted`, `private`, `direct`. For detailed information, see [official documentation](https://github.com/tootsuite/documentation/blob/master/Using-Mastodon/User-guide.md#toot-privacy)

### Clipboard image (1.0-4)

- Append image from clipboard, by adding `!clipboard:` or `!cb:`

### Reply to (1.0-5)

- Reply to toot with status id, add `!to:` and status id at the back
- i.e. `status content !to: 1002345678910111213`

### Line break (1.0-5)

- Switched to multiple line input window
- may change workflow when working with keyboard shortcut; just pressing return key would not send toot - tab - tab - space will do though
- if not in fond with this behaviour, you can use [version 1.0-4](https://github.com/Canorus/alfred-toot/raw/master/old/Alfred-toot_1.0-4.alfredworkflow) from `old` directory. Line break will not work. I will work on it tho, no ETA.

### Reply to mention (1.0-6)

- keyword `mreply` will list mentions you got, and type your reply and hit return.
- Since this feature uses Script filter, you might want to wait couple of seconds before hitting return key. This might change in the future.

------

### Todo

- [ ] Toot ending with exclamation mark. This is **urgent**
- [x] `reply` to notification hmm
- [ ] `-web`
- [x] ~~Contents warning message~~
- [ ] multiple accounts
- [x] ~~visibility~~
- [x] ~~line break~~
- [x] ~~Append single image from clipboard~~
- [x] ~~reply to~~

------

### Changelog

- 1.0-5
  - switched to multiline input popup for line break; may change keyboard shortcut
  - reply to toot with toot id
  - updated Changelog
- 1.0-4
  - added attaching single image from clipboard
- 1.0-3
  - added visibility option on sending toot
- 1.0-1
  - added Content Warning
  - added workflow icon

------

As always, any pull requests or ideas will be appreciated. If you have problem, please contact me on [twingyeo](https://twingyeo.kr/@canor) or [cmx](https://cmx.im/@canor).
