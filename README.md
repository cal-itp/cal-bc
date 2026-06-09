# Cal-B/C

This tool calculates values based on Cal-B/C workbooks. It also provides automation around filling out workbooks.


## Installation

> [!NOTE]
> All commands below should be run inside this directory.

This application requires `uv` to be installed. This can be installed using [asdf](https://asdf-vm.com):

```bash
$ asdf plugin add uv
$ asdf install
```

Install dependencies using `uv`:

```bash
$ uv sync
```

Copy `.env.example` to `.env` and fill in the secret values in the `.env` file:

```bash
$ cp .env.example .env
```

Set your Google Cloud project and login:

```bash
$ gcloud config set project cal-itp-data-infra-staging # you will want to unset this later with `gcloud config unset project`
$ gcloud auth application-default login --login-config=iac/login.json --quiet
```

Create the database and run migrations:

```bash
$ uv run manage.py sqlcreate | psql
$ uv run manage.py migrate
```

> [!NOTE]
> If you don't have postgresql, run `brew install postgresql` or visit https://www.postgresql.org/ for more information.
>
> If you run into the error `database "database_name" does not exist`, you may need to create it manually running `createdb <database_name>`.
>
> To check if your database was created, run `psql -l`.

In another terminal tab, start the Tailwind build process:

```bash
$ uv run manage.py tailwind build
$ uv run manage.py tailwind watch
```

Then, collect all the static files and start the Django server:

```bash
$ uv run manage.py collectstatic
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

> [!NOTE]
> You can run only the web application tests using:
>
> ```bash
> $ uv run manage.py test tests/cal_bc
> ```


### Linting

This project uses [ruff](https://astral.sh/ruff) to lint code. To run linting and apply fixes:

```bash
$ uv run ruff check --fix
```


### Administering the site locally

In order to access the admin site at [http://localhost:8000/admin](http://localhost:8000/admin), you need to create a superuser for your DOT login:

```bash
$ uv run manage.py createsuperuser
Username (leave blank to use 'yourname'): Your.Name@dot.ca.gov
Email address: Your.Name@dot.ca.gov
Password: ********
Password (again): ********
```

Now, when you visit the admin site, you can log in with your DOT account as usual.

> [!NOTE]
> If you forget to add your user before this point, the Azure Entra ID login package will automatically add a user and disallow access. You will need to either manually make your user a superuser or delete your user account.


## License

This tool is licensed under the terms of the GNU Affero General Public License.
