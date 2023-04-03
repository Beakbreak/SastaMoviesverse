import classes from './Navmenu.module.css';

const Navmenu = props => {
    return (<><div className={classes.navigation}>
        <ul className={classes.ul}>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><i className={`fa-solid fa-house`}></i></span>
                    <span className={classes.title}>Home</span>
                </a>
            </li>
            {/* <!-- <li>
                <a href="#">
                    <span className={classes.icon"></span>
                    <span className={classes.icon">Home</span>
                </a>
            </li> --> */}
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><i className={`fa-solid fa-user`}></i></span>
                    <span className={classes.title}>Profile</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><i className={`fa-solid fa-sparkles`}></i></span>
                    <span className={classes.title}>Suggested</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><i className={`fa-solid fa-circle-info`}></i></span>
                    <span className={classes.title}>Most Rated</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><i className={`fa-solid fa-gear`}></i></span>
                    <span className={classes.title}>Trending</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><i className={`fa-solid fa-lock`}></i></span>
                    <span className={classes.title}>All Genres</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><i className={`fa-solid fa-circle-info`}></i></span>
                    <span className={classes.title}>About Us</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><i className={`fa-solid fa-right-from-bracket`}></i></span>
                    <span className={classes.title}>SignOut</span>
                </a>
            </li>
        </ul>
    </div></>);
}

export default Navmenu;