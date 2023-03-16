import bgvid from './bgvid2.mp4';
import classes from './Page.module.css';
import Buttons from '../Buttons';
import Login from './Login';
import { useState } from 'react';
const Page = () => {
    const [displayForm, setDisplayForm] = useState(false);
    const [fade, setFade] = useState(false);

    let fadeDiv = null;
    const clickhandler = (event) => {
        event.preventDefault();
        setFade(true);



        setTimeout(() => {
            setDisplayForm(true);
        }, 500);


    }
    if (fade) {
        fadeDiv = classes.fadeDiv;
    }


    return (<>

        <video className={classes.videoTag} autoPlay loop muted>
            <source src={bgvid} type='video/mp4' />
        </video>
        {!displayForm && <center className={fadeDiv}>
            <center className={classes.textHeading}>WELCOME TO MOVIEBIA</center>
            <center className={classes.mainText}>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam blandit laoreet dignissim. Maecenas placerat purus volutpat dictum cursus. Nam in viverra lacus, nec mattis purus. Sed tristique odio sed viverra porttitor. Maecenas feugiat quis tortor vitae laoreet. Nam at ligula.</center>
            <center><Buttons color="#18d907" clickhandler={clickhandler}>Get Started</Buttons></center>
        </center>}
        {displayForm && <Login />}


    </>)
}

export default Page;