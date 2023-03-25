import click

@click.group()
def commands():
    pass

# append data to the object
@click.command("append")
@click.argument("targetfile", type=click.Path(exists=True))
@click.option("-c", "--content", prompt="Enter the content", help="The content to write to the jpg file")
@click.option("-t", "--type", type=click.Choice(["txt", "exe"]), default="txt", help="The format of data to append")
def append_data(targetfile, content, type):

    with open(targetfile, 'ab') as target_file:
        # Check if user selected type is text input
        if type == "txt":
            target_file.write(content.encode())

        # Check if user wants to append file
        elif type == "exe":
            with open(content, 'rb') as source_file:
                target_file.write(source_file.read())


    click.echo(f"Successfully written data to file '{targetfile}'")


# delete all data from the target file
@click.command("delete")
@click.argument("targetfile", type=click.Path(exists=True))
def delete_data(targetfile):
    with open(targetfile, 'rb+') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))  # FFD9 end hex of jpg file
        f.seek(offset + 2)
        f.truncate()

        click.echo(f"Successfully deleted all written data from file '{targetfile}'")


# Extract data from jpg files
@click.command("extract")
@click.argument("targetfile", type=click.Path(exists=True))
@click.option("-t", "--type", type=click.Choice(["txt", "exe"]), default="txt", help="The format of data to extract")
@click.option("-d", "--destination", type=click.Path(exists=True), help="Target destination to store extracted executable")
def extract_data(targetfile, type, destination):
    with open(targetfile, 'rb') as f:

        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        f.seek(offset + 2)

        if type == "txt":
            try:
                text = f.read().decode()
                if text == "":
                    click.echo("No text found")
                else:
                    click.echo(text)
            except(UnicodeDecodeError):
                click.echo("Invalid type, see --help")


        elif type == "exe":

            # Default file name
            target_destination = "extracted_file.exe"

            # Update file name if user provided
            if destination is not None:
                target_destination = destination

            # Write bytes to file
            with open(target_destination, 'wb') as extracted_exe:
                extracted_exe.write(f.read())
                click.echo("Written extracted executable")


commands.add_command(extract_data)
commands.add_command(delete_data)
commands.add_command(append_data)

if __name__ == '__main__':
    commands()
