import bgvid from './bgvid2.mp4';
import classes from './Page.module.css';
const Page = () => {
    return (<>

        <video className={classes.videoTag} autoPlay loop muted>
            <source src={bgvid} type='video/mp4' />
        </video>
    </>)
}

export default Page;