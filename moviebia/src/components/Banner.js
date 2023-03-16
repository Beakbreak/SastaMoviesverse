import classes from './Banner.module.scss';
const Banner = props => {
    return (<div className={classes.main1}>
        <ul className={classes.ul}>
            <li className={classes.li}>
                {/* <div className={classes.slidetitle}> */}
                {/* <span className={classes.span}>Kung-Fu Panda</span> */}
                {/* </div> */}
                <a href='#'>
                    <img className={classes.img} src="https://i.imgur.com/lwYJ4rx.jpg" />
                </a>
            </li>
            <li className={classes.li}>
                {/* <div className={classes.slidetitle}> */}
                {/* <span className={classes.span}>Toy Story</span> */}
                {/* </div> */}
                <a href='#'>
                    <img className={classes.img} src="https://i.imgur.com/BjB65TS.jpg" />
                </a>
            </li>
            <li className={classes.li}>
                {/* <div className={classes.slidetitle}> */}
                {/* <span className={classes.span}>Wall-E</span> */}
                {/* </div> */}
                <a href='#'>
                    <img className={classes.img} src="https://i.imgur.com/nyettOe.jpg" />
                </a>
            </li>
            <li className={classes.li}>
                {/* <div className={classes.slidetitle}> */}
                {/* <span className={classes.span}>Up</span> */}
                {/* </div> */}
                <a href='#'>
                    <img className={classes.img} src="https://i.imgur.com/WBTntRU.jpg" />
                </a>
            </li>
            <li className={classes.li}>
                {/* <div className={classes.slidetitle}> */}
                {/* <span className={classes.span}>Cars 2</span> */}
                {/* </div> */}
                <a href='#'>
                    <img className={classes.img} src="https://i.imgur.com/QwnE7FX.jpg" />
                </a>
            </li>
            <li className={classes.li}>
                {/* <div className={classes.slidetitle}> */}
                {/* <span className={classes.span}>Cars 2</span> */}
                {/* </div> */}
                <a href='#'>
                    <img className={classes.img} src="https://i.imgur.com/QwnE7FX.jpg" />
                </a>
            </li>
            <li className={classes.li}>
                {/* <div className={classes.slidetitle}> */}
                {/* <span className={classes.span}>Cars 2</span> */}
                {/* </div> */}
                <a href='#'>
                    <img className={classes.img} src="https://i.imgur.com/QwnE7FX.jpg" />
                </a>
            </li>
        </ul>
    </div>);
}
export default Banner;