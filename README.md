## Description
Gilg is a tool for bulk downloading media from websites, utilizing gallery-dl. It lets you easily update whole set of directiories with newly posted pictures or videos on a site with single command.

## 0. Install requierements
You need to install couple of things before you proceed:
- Download python from official source: [Link](https://www.python.org/downloads/)
- Install gallery-dl by running this command `pip install gallery-dl`

done.

## 1. Choosing browser

Set browser that gallery-dl should extract cookies from. Replace <browser_name> with name of the desired browser for example "chrome".

```bash
gilg --setting browser --value chrome
```

You can view all available browsers by using this command.
```bash
gilg --list-settings
```
 You can find them by searching for "browser" setting and looking at "Allowed Values" category.

## 2. Making a pack

Pack is a list of items that include:
- Name : The name of the item.
- Folder : The exact directory where gallery-dl should download the files
- Link : The URL that gallery-dl should use to download the files from

Create a new pack. Replace <pack_name> with desired name of the pack.
```bash
gilg --new <pack_name>
```

Example:
```bash
gilg --new InstagramArtists
```

You can list all packs to confirm that your pack was indeed created.
```bash
gilg --list-packs
```

You created a pack where items will be stored.


## 3. Creating an Item

Now you need to create an item
```bash
gilg --add <pack_name> --name <item_name> --folder <path> --link <URL>
```

Example:
```bash
gilg --add InstagramArtists --name HaxoTF --folder C:\\Users\\Bob\\Desktop\\HaxoTF --link https://www.instagram.com/haxotf/
```

To confirm that item was created use:
```bash
gilg --list-items <pack_name>
```

## 5. Updating directory

This is the part where you can finally download media files automatically from a list:
```bash
gilg --update <pack_name>
```
It will run `gallery-dl --cookies-from-browser <browser> -D <item_folder> <item_link>` command repeatedly by using items properties