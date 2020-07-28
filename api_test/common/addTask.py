import re

from crontab import CronTab
import logging

def add(host_id, _type, start_time, end_time, project, frequency=None, unit=None):
    """
    添加测试任务到crontab
    :param host_id:  测试域名
    :param _type:  执行类型
    :param start_time:  执行时间
    :param end_time:  结束时间
    :param frequency:  时间间隔
    :param unit:  时间单位
    :param project:  项目ID
    :return:
    """
    logging.info("创建定时任务,时间转换前{}--->{}".format(start_time,end_time))
    start_time = re.split('-|:| ', start_time)
    end_time = re.split('-|:| ', end_time)
    # 创建当前用户的crontab，当然也可以创建其他用户的，但得有足够权限
    logging.info("创建定时任务{}--->{}".format(start_time,end_time))
    my_user_cron = CronTab(user=True)
    my_user_cron.remove_all(comment=project)
    my_user_cron.remove_all(comment=project+"_开始")
    my_user_cron.remove_all(comment=project+"_结束")
    # for j in my_user_cron.crons:
    if _type == 'timing':
        _time = '%s %s %s %s *' % (
            start_time[4],
            start_time[3],
            start_time[2],
            start_time[1],
        )
        job = my_user_cron.new(command='../api_test/common/auto_test.py %s %s >> ../%s.log'
                                       % (host_id, project, project))
        logging.info("addtask_type=timing{}".format(_type))
    else:
        _time = '%s %s %s %s *' % (
            start_time[4],
            start_time[3],
            start_time[2],
            start_time[1],
        )
        logging.info("addtask_type=else{}".format(_type))
        #  创建任务
        job = my_user_cron.new(command='/usr/local/python3/bin/python3 /var/lib/jenkins/workspace/'
                                       'api_automation_test_master-JU72M6SAEYKDY6SN3LUUPLXPTX3F35MVFZ5'
                                       '7J4JE3I5TJCTRFXHQ/api_test/common/auto_start.py %s %s %s %s %s %s %s %s >> '
                                       '/var/lib/task/%s.log'
                                       % (frequency, unit, host_id, end_time[4], end_time[3],
                                          end_time[2], end_time[1], project, project))
    logging.info("创建了定时任务{}--{}".format(job,_time))
    job.set_comment(project+"_开始")
    # 设置任务执行周期
    job.setall(_time)
    logging.info("设置任务执行周期完成")
    # 最后将crontab写入配置文件
    my_user_cron.write()
    logging.info("任务周期写入配置文件")
