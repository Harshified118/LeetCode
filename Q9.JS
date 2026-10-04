let check= false;
login =(attempts, correctPassword="1234") => {
    for (let j =0; j <=4;j++ ) {
        for (const i of (attempts)) {
            if (i == correctPassword) {
                console.log("Correct Password")
                check =true
                break;
            }
            else if (i=="")
                      continue;
            
            else {
                console.log("Invalid Password")
            }
        }

    if (check=true) {
        console.log("Account Lock")
    }
    }
}
login(['1111','5678','',1234])