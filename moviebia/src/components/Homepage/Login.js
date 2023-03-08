import classes from "./Login.module.css";
import { useState } from 'react';
const Login = (props) => {
    const [displayLogin, setDisplayLogin] = useState(true);
    const signupToggle = (event) => {
        event.preventDefault();
        setDisplayLogin(false);
    }
    const loginToggle = (event) => {
        event.preventDefault();
        setDisplayLogin(true);
    }
    return (
        <div className={classes.container}>
            <div className={classes.form}>
                <div className={classes.btn}>
                    <button className={classes.signUpBtn} onClick={signupToggle}>SIGN UP</button>
                    <button className={classes.loginBtn} onClick={loginToggle}>LOG IN</button>
                </div>
                {!displayLogin && <form className={classes.signUp} action="" method="get">
                    <div className={classes.formGroup}>
                        <input type="text" id="userName" placeholder="User Name" autocomplete="off" />
                    </div>
                    <div className={classes.formGroup}>
                        <input type="email" placeholder="Email ID" name="email" required autocomplete="off" />
                    </div>
                    <div className={classes.formGroup}>
                        <input type="password" id="password" placeholder="Password" required autocomplete="off" />
                    </div>
                    <div className={classes.formGroup}>
                        <input type="password" id="confirmPassword" placeholder="Confirm Password" required autocomplete="off" />
                    </div>
                    <div className={classes.checkBox}>
                        <input type="checkbox" name="checkbox" id="checkbox" />
                        <span className={classes.text}>I agree with term & conditions</span>
                    </div>
                    <div className={classes.formGroup}>
                        <button type="submit" className={classes.btn2}>REGISTER</button>
                    </div>

                </form>}


                {displayLogin && <form className={classes.login} action="" method="get">

                    <div className={classes.formGroup}>
                        <input type="email" placeholder="Email ID" name="email" required autocomplete="off" />
                    </div>
                    <div className={classes.formGroup}>
                        <input type="password" id="password" placeholder="Password" required autocomplete="off" />

                    </div>
                    <div className={classes.checkBox}>
                        <input type="checkbox" name="checkbox" id="checkbox" />
                        <span className={classes.text}>Keep me signed in on this device</span>
                    </div>
                    <div className={classes.formGroup}>
                        <button type="submit" className={classes.btn2}>LOGIN</button>
                    </div>

                </form>}

            </div>
        </div>
    );
}

export default Login;