curl http://localhost:5001/

curl -H "Content-Type: application/json" -X POST -d '{"cyl":"8","disp":"250.3","hp":"156","drat":"4.43","wt":"3.221","qsec":"14.98","vs":"0","am":"0","gear":"4","carb":"2"}' "http://localhost:5001/mtcars_predict"