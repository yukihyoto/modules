import time
///
#!/usr/bin/perl

$goal = 1000000;

while (1) {

    $before = time();

    for ($i = 0; $i < $goal; $i ++) {

        $x = 0.000001;

        $y = sin($x);

        $y = $y + 0.00001;

    }

    $y += 0.01;

    # print "One million sin: ", time() - $before, " seconds!\n";

}
///
