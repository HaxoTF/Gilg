### 1. Listing settings
First thing you will need to do is to look up at available settings of course to get the idea what you can change. To do that type `gilg --list-config` in the terminal. It should display bunch of options

- `Name` a name of specific setting that you will refer with
- `value` current value of a setting

Some values might have couple words separated by space. That means the setting allowes only specific values. The green one is the one that is currently active.

### 2. Changing the setting
Every setting has it's default value set before you, but you can change them by simple command. Type `gilg -sc -n "name_of_setting" -b "new_value"` in the console to change its current value.

---
### Settings
- `browser` : the specific browser gallery-dl should extract cookies from. It uses the fact you are already logged in on your browser and uses your login information to get access to media you want to download.
- `default_root` : defines the **default** location of Gilg downloads. You can replace items "--folder" with "default" to use default location instead. When you use --list-items the special variables should appear in purple to confirm you indeed typed them correctly.