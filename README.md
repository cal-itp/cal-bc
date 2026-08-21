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

Finally, start the Django tasks worker:

```bash
$ uv run manage.py db_worker
```

Now, visit the server at [http://localhost:8000](http://localhost:8000).


### Linting

This project uses [ruff](https://astral.sh/ruff) to lint code. To run linting and apply fixes:

```bash
$ uv run ruff check --fix
```


### Testing

In order to run tests, you will need to ensure that [Playwright](https://playwright.dev) is installed:

```bash
$ uv run playwright install
```

Now, run the tests:

```bash
$ uv run manage.py test
```

> [!NOTE]
> Remember to add new pages or components to [/tests/cal_bc/system/test_accessibility_system.py](https://github.com/cal-itp/cal-bc/blob/main/tests/cal_bc/system/test_accessibility_system.py).<br>
> Accessibility reports can be found locally in the `axe-results/` folder.


Additional options you can add to the test command:

* To run only the web application tests, use:

  ```bash
  $ uv run manage.py test tests/cal_bc
  ```

* To run a specific file, add the file path. For example:

  ```bash
  $ uv run manage.py test tests/cal_bc/system/test_model_system.py
  ```

* To run a specific test, add the file path separating the test name with double colons `::`. For example:

  ```bash
  $ uv run manage.py test tests/cal_bc/models/test_model.py::TestModel::test_version_has_form_link
  ```


If a Playwright test fails, you can find screenshots and videos locally in the `cal-bc/test-results/` folder.

Playwright executes tests in a "headless" state, meaning it runs in the background without opening a user interface.
If you want Playwright tests in a visible browser window use the `-- --headed` flag. You can change the velocity of the test adding `--slowmo <milliseconds>`.

For example:

```bash
$ uv run manage.py test tests/cal_bc/system/test_model_system.py -- --headed --slowmo 2000
```


#### VCR / Cassette files

If you are testing features that makes HTTP requests, you need to include the decorator `@pytest.mark.vcr` before your test definition.
The Pytest VCR records your HTTP requests and responses into a cassette file so they can be replayed offline during future test runs.
Cassette files are created inside `cassettes\` folder located in the same folder as your test file.

To run for the first time, or if you deleted the cassette file, add `-- --record-mode=once` after the test command. For example:

```bash
$ uv run manage.py test tests/cal_bc/system/test_accessibility_system.py -- --record-mode=once
```

To update a cassette file add `-- --record-mode=rewrite` after the test command. For example:

```bash
$ uv run manage.py test tests/cal_bc/system/test_project_system.py  -- --record-mode=rewrite
```


### Managing Django in Cloud Run

To run `manage.py` commands on the deployed Cloud Run instance, use the [cal-bc-staging-manage](https://console.cloud.google/run/jobs/details/us-west2/cal-bc-staging-manage) Cloud Run Job.

For example, if you want to migrate the `models` app back to a specific migration, you would locally run:
```bash
$ uv run manage.py migrate models 0013_subsection_description
```

The Cloud Run Jobs equivalent using `cal-bc-staging-manage` is:
```bash
$ gcloud run jobs execute cal-bc-staging-manage --args migrate,models,0013_subsection_description --wait
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

To access or make changes to your local database, run:

```bash
$ uv run manage.py dbshell
```

To reset your local database, run:

```bash
$ uv run manage.py reset_db
```

## License

This tool is licensed under the terms of the GNU Affero General Public License.
