# mtcars Flask API

To run this project, open this directory in shell and run the following command to build the docker image (if this is your first time running it) and container:

`docker compose up -d`

Once you finish building, you can run the following command to check if the server is running properly:

`curl http://localhost:5001/`

This project uses the `mtcars` dataset and predicts the `mpg` of the vehicles using the following variables (all numerical, original description can be found [here](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html)):
- `cyl`: Number of cylinders
- `disp`: Displacement (cu.in.)
- `hp`: Gross horsepower
- `drat`: Rear axle ratio
- `wt`: Weight (1000 lbs)
- `qsec`: 1/4 mile time
- `vs`: Engine (0 = V-shaped, 1 = straight)
- `am`: Transmission (0 = automatic, 1 = manual)
- `gear`: Number of forward gears
- `carb`: Number of carburetors

You must provide all variables in the format of a Python dictionary. All variables and values must be wrapped in quotation marks, with no space in between them. Here is an example:

`'{"cyl":"8","disp":"250.3","hp":"156","drat":"4.43","wt":"3.221","qsec":"14.98","vs":"0","am":"0","gear":"4","carb":"2"}'`

You can try to predict the `mpg` using the example above with the following command:

`curl -H "Content-Type: application/json" -X POST -d '{"cyl":"8","disp":"250.3","hp":"156","drat":"4.43","wt":"3.221","qsec":"14.98","vs":"0","am":"0","gear":"4","carb":"2"}' "http://localhost:5001/mtcars_predict"`

If your command runs successfully, the predicted `mpg` should be approximately 17.44.

The above commands can be found in `example.sh`. You can run this script using the following command:

`bash example.sh`

To close the project, run the following command:

`docker compose down -v`
