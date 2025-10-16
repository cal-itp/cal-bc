# Cal-B/C

This tool calculates values based on Cal-B/C workbooks. It also provides automation around filling out workbooks.


## Installation

> Note: All commands below should be run inside this directory.

This application requires `uv` to be installed. This can be installed using [asdf](https://asdf-vm.com):

```bash
$ asdf plugin add uv
$ asdf install
```

Install dependencies using `uv`:

```bash
$ uv install
```

Copy `.env.example` to `.env`, fill in the secret values in the `.env` file:

```bash
$ cp .env.example .env
```

In one terminal tab, start the Tailwind build process:

```bash
$ uv run manage.py tailwind watch
```

In another terminal tab, run migrations and start the server:

```bash
$ uv run manage.py migrate
$ uv run manage.py runserver
```

Now, visit the server at [http://localhost:8000](http://localhost:8000).


### Running tests

In order to run tests, you will need to ensure that [Playwright](https://playwright.dev) is installed:

```bash
$ uv run playwright install
```

Now, run the tests:

```bash
$ uv run manage.py test
```

> Note: you can run only the web application tests using:
>
> ```bash
> $ uv run manage.py test tests/cal_bc
> ```


## License

This tool is licensed under the terms of the GNU Affero General Public License.
