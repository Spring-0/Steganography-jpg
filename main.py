import click

@click.group()
def commands():
    pass

# append data to the object
@click.command("append")
@click.argument("targetfile", type=click.Path(exists=True))
@click.option("-c", "--content", prompt="Enter the content", help="The content to write to the file")
def append_data(targetfile, content):
    with open(targetfile, 'ab') as f:
        f.write(content.encode())

    click.echo(f"Successfully written content to file '{targetfile}'")


# delete data from the object
@click.command("delete")
@click.argument("targetfile", type=click.Path(exists=True))
def delete_data(targetfile):
    with open(targetfile, 'rb+') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))  # FFD9 end hex of jpg file
        f.seek(offset + 2)
        f.truncate()

        click.echo(f"Successfully deleted all written data from file '{targetfile}'")


# Extract the data from jpg files
@click.command("extract")
@click.argument("targetfile", type=click.Path(exists=True))
def extract_jpg(targetfile):
    with open(targetfile, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        f.seek(offset + 2)

        click.echo(f.read().decode())


commands.add_command(extract_jpg)
commands.add_command(delete_data)
commands.add_command(append_data)

if __name__ == '__main__':
    commands()
