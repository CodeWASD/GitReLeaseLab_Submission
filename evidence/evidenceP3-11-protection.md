# P3.11 — Branch Protection Verification

## Protection Configuration

Available: YES

Protection Type: Repository Ruleset  
Ruleset Name: Protect master with CI  
Target Branch: master  
Enforcement Status: Active  
Required Status Check: Run pytest  

## Failing CI Verification

Branch: lab/protection-test  
Failing Commit SHA: d9155338a8831631eb9a382f8c05b65d9139bc36  
Failed Workflow: Python CI  
Failed Job: Run pytest  
Failed Test: test_category_default_behavior  
Failure Cause: The test expected `wrong-category`, but the application returned `general`.  
CI Result: FAIL  
Merge Status: BLOCKED  

## Fixed CI Verification

Fix Commit SHA: 354ca6497c10d146583e1cef8ddc04265aba279f  
Fix Description: Restored the expected default category from `wrong-category` to `general`.  
Local Test Result: 3 passed  
CI Result: PASS  
Merge Status After CI Passed: ALLOWED  

## Conclusion

The repository ruleset successfully prevented merging while the required CI check was failing. After a corrective commit passed the required `Run pytest` check, GitHub allowed the pull request to be merged.